import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# 1. Testar se uma questão começa sem nenhuma alternativa cadastrada
def test_question_starts_with_no_choices():
    question = Question(title='Matemática')
    assert len(question.choices) == 0

# 2. Testar se o título passado é salvo igual
def test_question_title_is_saved_correctly():
    question = Question(title='Qual a capital de MG?')
    assert question.title == 'Qual a capital de MG?'

# 3. Testar se adicionar duas alternativas atualiza o tamanho da lista para 2
def test_add_multiple_choices_updates_count():
    question = Question(title='Cores')
    question.add_choice('Azul', False)
    question.add_choice('Vermelho', True)
    assert len(question.choices) == 2

# 4. Testar se a ordem das alternativas é mantida (a primeira a entrar fica na posição 0)
def test_choice_order_is_preserved():
    question = Question(title='Letras')
    question.add_choice('A', True)
    question.add_choice('B', False)
    assert question.choices[0].text == 'A'
    assert question.choices[1].text == 'B'

# 5. Testar se o sistema registra corretamente uma alternativa como verdadeira
def test_add_correct_choice():
    question = Question(title='1 + 1?')
    question.add_choice('2', True)
    assert question.choices[0].is_correct == True

# 6. Testar se o sistema registra corretamente uma alternativa como falsa
def test_add_incorrect_choice():
    question = Question(title='1 + 1?')
    question.add_choice('3', False)
    assert question.choices[0].is_correct == False

# 7. Testar se a questão aceita textos com caracteres especiais
def test_choice_with_special_characters():
    question = Question(title='Símbolos')
    question.add_choice('@#$%', False)
    assert question.choices[0].text == '@#$%'

# 8. Testar se pode-se criar uma questão passando uma pontuação específica
def test_question_custom_points():
    question = Question(title='Questão Difícil', points=10)
    assert question.points == 10

# 9. Testar se alterar o título de uma questão depois que ela já foi criada funciona
def test_change_question_title():
    question = Question(title='Título Antigo')
    question.title = 'Título Novo'
    assert question.title == 'Título Novo'

# 10. Testar se é possível adicionar uma alternativa com texto vazio
def test_choice_with_empty_text():
    question = Question(title='Vazio')
    with pytest.raises(Exception) as info_do_erro:
        question.add_choice('', False)
    assert str(info_do_erro.value) == 'Text cannot be empty'


# PARTE 3: Testes usando Fixtures

@pytest.fixture
def question_with_choices():
    question = Question(title='Quanto é 2 + 2?')
    question.add_choice('3', False)
    question.add_choice('4', True)
    question.add_choice('5', False)
    
    return question

def test_fixture_choices_count(question_with_choices):
    assert len(question_with_choices.choices) == 3

def test_fixture_correct_choice(question_with_choices):
    correct_choice = question_with_choices.choices[1]
    
    assert correct_choice.is_correct == True
    assert correct_choice.text == '4'