real_ans = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
      guess_a_number = int(input('Guess : '))
      guess_count += 1
      if guess_a_number == real_ans:
         print('you win')
         break
else:
    print('sorry you failed')


      