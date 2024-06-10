a=int(input("how many courses :\n"))
grp=[]
cr=[]
st=[]
for i in range((a)):
    grp.append(int(input("course grade points : ")))
    cr.append(int(input("no.of credits : ")))
    st.append(grp[i]*cr[i])
print("SGPA points is : ",sum(st)/sum(cr))