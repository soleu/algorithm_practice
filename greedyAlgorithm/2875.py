
# 백준대학교에서는 대회에 나갈 때 2명의 여학생과 1명의 남학생이 팀을 결성해서 나가는 것이 원칙이다. (왜인지는 총장님께 여쭈어보는 것이 좋겠다.)

# 백준대학교는 뛰어난 인재들이 많아 올해에도 N명의 여학생과 M명의 남학생이 팀원을 찾고 있다. 대회에 참여하려는 학생들 중 K명은 반드시 인턴쉽 프로그램에 참여해야 한다. 인턴쉽에 참여하는 학생은 대회에 참여하지 못한다.

# 백준대학교에서는 뛰어난 인재들이 많기 때문에, 많은 팀을 만드는 것이 최선이다.

# 여러분은 여학생의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K가 주어질 때 만들 수 있는 최대의 팀 수를 구하면 된다.

n,m,k=map(int,input().split()) 
totalMember=n+m
TeamNumber= min(n//2,m)
remainMember=totalMember-TeamNumber*3
intershipMember=0
if(remainMember<k):
    k-=remainMember 
    intershipMember=(k//3)
    if(k%3>0) : intershipMember+=1

print(TeamNumber-intershipMember)
# print(minNum-intershipMember)