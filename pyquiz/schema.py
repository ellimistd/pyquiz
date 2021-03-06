"""
This file is used to create the schema used for the test
creation form.
"""

from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Schema
from colander import Date
from colander import Range

from deform import ValidationFailure
from deform import Form
from deform import widget

class EditAnswerSchema(MappingSchema):
    """
    Schema that stores a single answer to a question.
    """
    text = SchemaNode(String())
    correct = SchemaNode(Boolean())
    remove = SchemaNode(Boolean())

class EditAnswers(SequenceSchema):
    """
    Schema used to store the sequence AnswerSchema classes
    for each quesiton in the test.
    """
    answers = EditAnswerSchema()

class EditQuestionSchema(MappingSchema):
    """
    Schema that stores a single question to a test.
    """
    text = SchemaNode(String())
    remove = SchemaNode(Boolean())
    answers = EditAnswers()

class EditShortAnswerQuestionSchema(MappingSchema):
    """
    Schema that stores a short answer question.  Does not have an answer.
    """
    text = SchemaNode(String())
    remove = SchemaNode(Boolean())


class AnswerSchema(MappingSchema):
    """
    Schema that stores a single answer to a question.
    """
    text = SchemaNode(String())
    correct = SchemaNode(Boolean())

class Answers(SequenceSchema):
    """
    Schema used to store the sequence AnswerSchema classes
    for each quesiton in the test.
    """
    answers = AnswerSchema()

class QuestionSchema(MappingSchema):
    """
    Schema that stores a single question to a test.
    """
    text = SchemaNode(String())
    answers = Answers()

class ShortAnswerQuestionSchema(MappingSchema):
    """
    Schema that stores a short answer question.  Does not have an answer.
    """
    text = SchemaNode(String())

class ShortAnswerQuestions(SequenceSchema):
    """
    Schema used to store the sequence of ShortANswerQuestionSchema
    classes representing each short answer quesiton in the test.
    """
    questions = ShortAnswerQuestionSchema()

class Questions(SequenceSchema):
    """
    Schema used to store the sequence of QuestionSchema
    classes representing each quesiton in the test.
    """
    questions = QuestionSchema()

class AddQuestionsSchema(Schema):
    questions = Questions()
    short_answer_questions = ShortAnswerQuestions()

class TestSchema(Schema):
    """
    Schema that stores the test being created.
    """
    import datetime
    name = SchemaNode(String())
    attempts = SchemaNode(String())
    start_date =SchemaNode( Date(),
                validator=Range(
                    min=datetime.datetime.now(),
                    min_err=('${val} is earlier than earliest date ${min}')))
    end_date = SchemaNode( Date(),
                validator=Range(
                    min=datetime.datetime.now(),
                    min_err=('${val} is earlier than earliest date ${min}')))
    questions = Questions()
    short_answer_questions = ShortAnswerQuestions()


