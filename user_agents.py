import random

class GetUserAgentsCsv:
    def __init__(self):
        self.all_user_agents = []
        
    def set_all_user_agents(self):
        with open('newuseragents.csv', newline='\n') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the first line (header)
            next(reader)
            for row in reader:
                # Assuming the user agents are in the first column of the CSV
                self.all_user_agents.append(row[0])

    def shuffleAgents(self):
        # Shuffle the array randomly
        random.shuffle(self.all_user_agents)

    def get_all_user_agents(self):
        self.set_all_user_agents()
        self.shuffleAgents()
        return self.all_user_agents