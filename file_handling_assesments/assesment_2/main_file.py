# with open(r'C:\Users\HP\OneDrive\Desktop\file_handling_assesments\assesment1\assesment_2\text.txt', 'r') as t,\
# open('chunkss.txt','w') as ch:
#     c=0
#     for line in t:
#         c+=1
#         # print(line.strip())
#         if c==2:
#             k=p_line+line.strip()
#             ch.write(f'{k}\n')
#             c=0
#         else:
#             p_line=line.strip()
def ask_question(question):
    max_score=0
    mrc=""
    with open('chunkss.txt', 'r') as file:            
        for word in question.split():
            score=0
            for chunk in file:
                if word.lower() in chunk.lower():
                    score+=1
            if score>max_score:
                max_score=score
                mrc=chunk
    print(mrc)
ask_question(input("What is your question? "))

        


