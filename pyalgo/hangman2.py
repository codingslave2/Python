# 행맨 게임
# - 단어의 각 글자 자리에 짧은 선이 그려진다.
# - 글자 1개를 맞추면 글자가 표시되고, 추가로 계속 맞추면 글자가 표시됨
# - 틀리면 기회가 1번 줄어든다.
# = 전체 글자를 입력하여 맞추면 프로그램이 바로 종료됨

import pygame
import random

words = ['dog', 'cat', 'monkey', 'chicken', 'frog', 'horse']
lives_remaning = 10 # 남은 기회(전역 변수)
guessed_letters = '' # 추측된 단어를 저장할 변수


def pick_a_word(): # 
    word = random.choice(words)
    return word

def get_guess(word):
    print_word_with_blanks(word)
    print("Lives Remaining " + str(lives_remaning))
    guess = input("Guess a letter or whole word? ") # 철자 or 단어 입력
    return 'a' 

def print_word_with_blanks(word):
    # print("아직 구현되지 않음")
    display_word = "" # 게이머가 추측한 글자가 입력될 변수
    for letter in word:
        if guessed_letters.find(letter) > -1: # 글자를 찾음
            display_word = display_word + letter # 단어를 추가해서 저장
        else:
            display_word = display_word + "-" # blank(밑줄) 추가함
    print(display_word)


def process_guess(guess, word):
    global lives_remaning # 지역변수인데 전역변수화함 (global)
    global guessed_letters # 추측됨

    lives_remaning = lives_remaning - 1 # 기회가 1 줄어듦
    guessed_letters += guess # 컴이 추측한 단어에 게이머가 입력한 글자가 추가됨
    if guess == word:
        return True # 프로그램
    return False # True로 변환하면 바로 종료

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word): #추측해서 맞췄을 때
            print("You Win! Well done")
            break

        if lives_remaning == 0:
            print("You are Hung")
            print("The word was: " + word)
            break

play()