class AnonymousSurvey():
    """collect anoonyomus answers to a survey questiob"""

    def __init__(self, question):
        """store a question, prepare for responses storage"""
        self.question = question
        self.responses = []

    def show_question(self):
        """shows the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """store a single response to a survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses"""
        print("Survey results:")
        for response in self.responses:
            print("\t- " + response)
