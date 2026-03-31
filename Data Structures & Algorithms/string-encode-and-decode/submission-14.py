class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for stra in strs:
            result+=str(len(stra))+"/t"+stra

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        j = 0
        # print(s)
        while i < len(s):
            # print(i)
            # print(s[i:i+1])            
            if s[i:i+2] == "/t":
                # print(s[i:])
                # print(left, "hi")
                # print(stra[left:i])
                length_of_word = int(s[j:i])
                # print(int(length_of_word))

                result.append(s[2 + i : 2+i+length_of_word])
                j+=2+length_of_word+len(str(length_of_word))
                i+=length_of_word+2
                # for j in range(wordlen):

                #     temp = ""
                    
                #     # for j in range(int(stra[i-1])):
                #     temp += stra[right+j]
                #     # print(stra[i+j+1])

                #     result.append(temp)

                # try:
                #     indexCount+=2+len(wordlen)
                # except:
                #     pass

            else:
                i+=1
        return result

            # resultword = ""
            # strb = stra.strip("2")
            # for char in strb:
            #     result.append(ord(char)-ord("a"))

            
            # result.append(resultword)
        # return result

        # for i in range(len(stra)):
        #     if stra[i:i+1] == "\t":
        #         # print(stra)
        #         temp = ""
        #         # print(stra[i-1:], temp)
        #         # print(int(stra[i-1]))
        #         for j in range(int(stra[i-1])):
        #             temp += stra[i+j+1]
        #             print(stra[i+j+1])

        #         result.append(temp)