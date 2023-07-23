def main():

        import random
        from HangmanStr import units
        from time import sleep


        words=['python','validation','network','architecture','hangman','structure','ability','youtube','variable','opreators','tuple','dictionary','purpose','marketing','smartphone','laptop','mainframe','supercomputers','progress','novels','widespread','amazon','kingfisher','']

        pickedword=random.choice(words)

        print('THE WORD HAS', len(pickedword),'letters')


        correct=['_'] * len(pickedword)
        incorrect=[]

        def modify():
            for i in correct:
                print(i, end = ' ')
            print()
        print('Let me guess a Word') 

        def wait():
          for i in range(5):
             print('.', end ='')
             sleep(.6)
          print()

        wait()
          
        modify() 
        units(len(incorrect))

        while True: 

            
          guess = input("Guess the letter :")
          print('Wait let me check')
          wait()
          if guess in pickedword:
             index = 0
             for i in pickedword:
                 if i == guess:
                    correct[index] = guess
                 index += 1
             modify()

          
          else:
             if guess not in incorrect:
                incorrect.append(guess)
                units(len(incorrect))
             else:
                print('Already Guessed')
             print(incorrect)
          if len(incorrect) > 4:
                 print('YOU LOSE')
                 print('The WORD IS',pickedword)
                 print("=========================================")
                 restart=input("Do you want to play again type yes :").lower()
                 if restart == "yes":
                      main()

                 else:
                    exit()
                 break
          if '_' not in correct:
              print('WINNER')
              print("=========================================")
              restart=input("Do you want to play again type yes :").lower()
              if restart == "yes":
                   main()

              else:
                  print('THE END')
                  exit()