class Solution:
    def romanToInt(self, s: str) -> int:
        RomanValuesList = [1,5,10,50,100,500,1000]
        RomanCharacters = ["I","V","X","L","C","D","M"]
        RomanDictionaryvalues = { key : value for key,value in zip(RomanCharacters,RomanValuesList)}
        sum = 0 
        j=0   
        while j<len(s):
            if(j==len(s)-1):
                sum += RomanDictionaryvalues[s[j]]
                j += 1
            else:    
                if(s[j] == "I"):
                    if(s[j+1] == "V")or(s[j+1] == "X"):
                        sum = sum+(RomanDictionaryvalues[s[j+1]]-RomanDictionaryvalues[s[j]]) 
                        j += 2
                    else:
                        sum = sum +RomanDictionaryvalues[s[j]] 
                        j += 1    
                elif(s[j]== "X"):
                    if(s[j+1] == "L")or(s[j+1] == "C"):     
                        sum = sum+(RomanDictionaryvalues[s[j+1]]-RomanDictionaryvalues[s[j]]) 
                        j += 2
                    else:
                        sum = sum +RomanDictionaryvalues[s[j]]  
                        j += 1   
                elif(s[j]== "C"):
                    if(s[j+1] == "D")or(s[j+1] == "M"):     
                        sum = sum+(RomanDictionaryvalues[s[j+1]]-RomanDictionaryvalues[s[j]])
                        j += 2
                    else:
                        sum = sum +RomanDictionaryvalues[s[j]]      
                        j += 1 
                else:
                    sum = sum +RomanDictionaryvalues[s[j]]   
                    j += 1          
        return sum