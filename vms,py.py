class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Poll:
    def __init__(self, question, options):
        self.question = question
        self.options = options
        self.votes = [0] * len(options)

class VotingSystem:
    def __init__(self):
        self.users = {}
        self.polls = {}

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            print("User registered successfully!")
        else:
            print("Username already exists.")

    def login(self, username, password):
        if username in self.users:
            if self.users[username].password == password:
                print("Login successful!")
                return True
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")
        return False

    def create_poll(self, username, question, options):
        if username in self.users:
            poll = Poll(question, options)
            self.polls[question] = poll
            print("Poll created successfully!")
        else:
            print("User not found. Please login first.")

    def vote_poll(self, username, question, option_index):
        if question in self.polls:
            poll = self.polls[question]
            poll.votes[option_index] += 1
            print("Vote successful!")
        else:
            print("Poll not found.")

    def show_poll_results(self, question):
        if question in self.polls:
            poll = self.polls[question]
            print("Poll Question:", poll.question)
            for i, option in enumerate(poll.options):
                print(f"{option}: {poll.votes[i]} votes")
        else:
            print("Poll not found.")

    def delete_poll(self, username, question):
        if username in self.users:
            if username == "admin":
                if question in self.polls:
                    del self.polls[question]
                    print("Poll deleted successfully!")
                else:
                    print("Poll not found.")
            else:
                print("You don't have permission to delete polls.")
        else:
            print("User not found.")

def main():
    voting_system = VotingSystem()
    
    # Register admin
    voting_system.register_user("admin", "admin123")
    
    while True:
        print("\nVoting Management System Menu:")
        print("1. Register User")
        print("2. Login")
        print("3. Create Poll")
        print("4. Vote on Poll")
        print("5. View Poll Results")
        print("6. Delete Poll (Admin)")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            voting_system.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if voting_system.login(username, password):
                current_user = username
        elif choice == '3':
            if 'current_user' in locals():
                question = input("Enter poll question: ")
                options = input("Enter poll options separated by commas: ").split(',')
                voting_system.create_poll(current_user, question, options)
            else:
                print("Please login first.")
        elif choice == '4':
            if 'current_user' in locals():
                question = input("Enter the poll question you want to vote on: ")
                if question in voting_system.polls:
                    poll = voting_system.polls[question]
                    print("Select an option to vote:")
                    for i, option in enumerate(poll.options):
                        print(f"{i + 1}. {option}")
                    option_choice = int(input("Enter the option number: ")) - 1
                    voting_system.vote_poll(current_user, question, option_choice)
                else:
                    print("Poll not found.")
            else:
                print("Please login first.")
        elif choice == '5':
            question = input("Enter the poll question you want to view results for: ")
            voting_system.show_poll_results(question)
        elif choice == '6':
            if 'current_user' in locals():
                if current_user == "admin":
                    question = input("Enter the poll question you want to delete: ")
                    voting_system.delete_poll(current_user, question)
                else:
                    print("Only admin can delete polls.")
            else:
                print("Please login first.")
        elif choice == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
