from mycroft import MycroftSkill, intent_file_handler


class LolQuestion(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('question.lol.intent')
    def handle_question_lol(self, message):
        self.speak_dialog('question.lol')


def create_skill():
    return LolQuestion()

