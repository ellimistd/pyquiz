selectTrueData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('name', u'Math Test'), ('class_id', u'Math 101'),
        ('__start__', u'questions:sequence'),
        ('__start__', u'questions:mapping'),
        ('text', u'1+1 = ?'), ('__start__', u'answers:sequence'),
        ('__start__', u'answers:mapping'), ('text', u'1'),
        ('correct', u'true'), ('__end__', u'answers:mapping'), 
        ('__start__', u'answers:mapping'), ('text', u'2'),
        ('correct', u'true'), ('__end__', u'answers:mapping'), 
        ('__end__', u'answers:sequence'), ('__end__', u'questions:mapping'),
        ('__end__', u'questions:sequence'), 
        ('__start__', u'short_answer_questions:sequence'), 
        ('__end__', u'short_answer_questions:sequence'),
        ('submit', u'submit')]

multipleChoiceData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'),
        ('name', u'Math Test'), ('class_id', u'Math 101'), 
        ('__start__', u'questions:sequence'), 
        ('__start__', u'questions:mapping'),
        ('text', u'1+1 = ?'), ('__start__', u'answers:sequence'),
        ('__start__', u'answers:mapping'), ('text', u'1'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'2'), ('correct', u'true'), ('__end__', u'answers:mapping'),
        ('__end__', u'answers:sequence'), ('__end__', u'questions:mapping'), 
        ('__end__', u'questions:sequence'), 
        ('__start__', u'short_answer_questions:sequence'), 
        ('__end__', u'short_answer_questions:sequence'),
        ('submit', u'submit')]

shortAnswerData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'),
        ('name', u'Short Answer'), ('class_id', u'Test'),
        ('__start__', u'questions:sequence'),
        ('__end__', u'questions:sequence'),
        ('__start__', u'short_answer_questions:sequence'),
        ('__start__', u'questions:mapping'),
        ('text', u"What is you're name?"), ('__end__', u'questions:mapping'),
        ('__end__', u'short_answer_questions:sequence'), ('submit', u'submit')]

allTypesData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('name', u'All Types'), ('class_id', u'Math 101'), 
        ('__start__', u'questions:sequence'),
        ('__start__', u'questions:mapping'), ('text', u'1+1 = ?'),
        ('__start__', u'answers:sequence'),
        ('__start__', u'answers:mapping'), ('text', u'1'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'2'), ('correct', u'true'), ('__end__', u'answers:mapping'),
        ('__end__', u'answers:sequence'), ('__end__', u'questions:mapping'),
        ('__start__', u'questions:mapping'), ('text', u'x^2 = 1'), 
        ('__start__', u'answers:sequence'),
        ('__start__', u'answers:mapping'), ('text', u'-1'),
        ('correct', u'true'), ('__end__', u'answers:mapping'), 
        ('__start__', u'answers:mapping'), ('text', u'1'), 
        ('correct', u'true'), ('__end__', u'answers:mapping'), 
        ('__start__', u'answers:mapping'), ('text', u'2'),
        ('__end__', u'answers:mapping'), ('__end__', u'answers:sequence'),
        ('__end__', u'questions:mapping'),('__end__', u'questions:sequence'), 
        ('__start__', u'short_answer_questions:sequence'),
        ('__start__', u'questions:mapping'), ('text', u"What is you're name?"),
        ('__end__', u'questions:mapping'),
        ('__end__', u'short_answer_questions:sequence'), ('submit', u'submit')]

addQuestionsData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('__start__', u'questions:sequence'), 
        ('__start__', u'questions:mapping'), ('text', u'2+2 = ?'),
        ('__start__', u'answers:sequence'), ('__start__', u'answers:mapping'),
        ('text', u'3'), ('__end__', u'answers:mapping'),
        ('__start__', u'answers:mapping'), ('text', u'4'),
        ('correct', u'true'), ('__end__', u'answers:mapping'),
        ('__end__', u'answers:sequence'), ('__end__', u'questions:mapping'), 
        ('__start__', u'questions:mapping'), ('text', u'X^2 = 4'), 
        ('__start__', u'answers:sequence'), ('__start__', u'answers:mapping'),
        ('text', u'-2'), ('correct', u'true'), ('__end__', u'answers:mapping'),
        ('__start__', u'answers:mapping'),('text', u'2'), ('correct', u'true'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'3'), ('__end__', u'answers:mapping'), 
        ('__end__', u'answers:sequence'), ('__end__', u'questions:mapping'),
        ('__end__', u'questions:sequence'), 
        ('__start__', u'short_answer_questions:sequence'),
        ('__start__', u'questions:mapping'), ('text', u'Who are you?'),
        ('__end__', u'questions:mapping'),
        ('__end__', u'short_answer_questions:sequence'), 
        ('add questions', u'add questions')]

editMultipleChoiceData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('text', u'X^2 = 4'), ('__star t__', u'answers:sequence'), 
        ('__start__', u'answers:mapping'), ('text', u'1'), ('remove', u'true'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'2'), ('correct', u'true'), ('remove', u'true'), 
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'), 
        ('text', u'X = -2'), ('correct', u'true'), 
        ('__end__', u'answers:mapping'),('__start__', u'answers:mapping'), 
        ('text', u'4'), ('remove', u'true'), ('__end__', u'answers:mapping'),
        ('__start__', u'answers:mapping'), ('text', u'X = 2'),
        ('correct', u'true'), ('__end__', u'answers:mapping'),
        ('__start__', u'answers:mapping'), ('text', u'6'), ('remove', u'true'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'X = 3'), ('__end__', u'answers:mapping'),
        ('__start__', u'answers:mapping'), ('text', u'X = 4'), 
        ('__end__', u'answers:mapping'), ('__end__', u'answers:sequence'),
        ('submit changes', u'submit changes')]

editSelectTrueData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('text', u'1+1=?'), ('__start_ _', u'answers:sequence'),
        ('__start__', u'answers:mapping'), ('text', u'1'), 
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'), 
        ('text', u'1'),('correct', u'true'), ('remove', u'true'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'2'), ('correct', u'true'), ('__end__', u'answers:mapping'),
        ('__start__', u'answers:mapping'), ('text', u'3'),
        ('__end__', u'answers:mapping'), ('__start__', u'answers:mapping'),
        ('text', u'4'), ('remove', u'true'), ('__end__', u'answers:mapping'), 
        ('__start__', u'answers:mapping'), ('text', u'4'),
        ('__end__', u'answers:mapping'), ('__end__', u'answers:sequence'), 
        ('submit changes', u'submit changes')]

editShortAnswerData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('text', u'Who are you?'), ('submit changes', u'submit changes')]

editRemoveQuestionData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('text', u'Who are you?'), ('remove', u'true'), 
        ('submit changes', u'submit changes')]

answerMultipleChoiceData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'),
        ('__start__', u'answer:rename' ), ('deformField1', u'2'), 
        ('__end__', u''), ('next question', u'next question')]

answerSelectTrueData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'), 
        ('__start__', u'answer:sequenc e'), ('checkbox', u'7'), 
        ('checkbox', u'8'), ('__end__', u'answer:sequence'),
        ('next question', u'next question')]

answerShortAnswerData = [('_charset_', u'UTF-8'), ('__formid__', u'deform'),
        ('answer', u'James Boisture'), ('review test', u'review test')]