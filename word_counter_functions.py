# Iver John R Monroy
# ITELEC2
# Laboratory # 23 - Group Activity # 01 - Problem 05: Word Counter in a Sentence with Input and Counting Functions
   



def main():
    
    sentence = input("Enter a sentence: ")
    word_count = len(sentence.split())
    print(f"The sentence has {word_count} words.")

if __name__ == "__main__":
    main()