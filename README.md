# developUs
---



## 대구시민을 위한 쓰레기 수거 서비스
![Desktop - 3](https://user-images.githubusercontent.com/81808787/192131075-4b080f3c-7acd-49af-99c5-0b1e0e9bf623.png)




### 팀명
_developUs_




### 제출 세션 및 주제
특별세션 - 도심 내 무단투기 쓰레기




### 프로젝트 한 줄 설명
맞춤형 쓰레기 수거 서비스를 웹으로 제공하여 도심 내 무단투기 쓰레기 및 분리수거 문제를 해결할 수 있다.





### 프로젝트에 대한 설명
  - 목적: 코로나 팬데믹으로 인한 언택트 소비의 활성화로 2020년 이후 쓰레기 배출량은 크게 늘었다. 그러나 늘어난 쓰레기 배출량에 비해 분리수거가 제대로 이루어지지 않아 재활용률이 낮다. 폐기물 업계는 '올바른 분리배출이 재활용률을 높이는 것에 있어서 가장 중요하다'라고 강조 했지만, 분리수거의 번거로움, 생활의 여유 부족 등의 이유로 주민들의 참여는 적극적으로 이루어지지 않을 뿐더러, 분리수거의 부담 때문에 쓰레기 무단투기까지 이어지기도 한다. 와르르는 이러한 쓰레기 분리 수거의 부담을 도맡아 쓰레기 배출 문제를 해결하고자 한다.
  
  
  - 서비스 내용: 쓰레기 종류, 배출량, 수거 날짜만 선택하면 간단하게 와르르의 쓰레기 수거 서비스를 이용할 수 있다. 정해진 수거 날짜에 맞추어 수거 기사가 방문하고, 현관이나 집 앞에 배출된 쓰레기를 수거하고, 업체에서 분리 수거를 한다. 또한 대구광역시에서 사용 가능한 지역화폐 카드인 대구행복페이 카드를 이용해 결제할 수 있다.
  
  
  - 영향: 음식물을 담았던 용기는 물로 씻은 후 버리고 페트병의 비닐 등을 제거하는 등, 제대로 된 분리수거는 생각보다 까다롭고 번거롭다. 와르르는 그 과정의 번거로움을 제거하고 올바른 방식으로 분리배출하여 재활용률을 높일 수 있다. 또한 지역화폐 카드인 대구행복페이 카드를 이용한 결제를 유도해 지역 내부의 경기를 활성화할 수 있다.




### 프로젝트에 활용된 기술



  - 우편번호 서비스
 
 <img src="https://img.shields.io/badge/kakao-FFCD00?style=for-the-badge&logo=kakao&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white">
     
     
   다음 우편번호 서비스를 이용했다. https://postcode.map.daum.net/guide 사이트와 html, css, js를 활용해서 서버 이용자의 주소 정보를 입력 받고 그 칸을 디자인했다. 


          
   - 로그인 및 회원가입 서비스
   
     <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
    
      
      mainClass : 유저 관리 클래스들의 모음
    
      User
        - 유저 정보 저장(saveUser) 및 비밀번호 받아오는(loadUser) 기능을 가진다.
    
      FindUser
        - 아이디 중복,존재 확인(fusearchId,searchId), pw가 맞는지 체크(checkPw)하는 기능을 가진다.
     
      위와 같은 클래스와 flask 및 파이썬을 활용해서 유저 로그인 및 회원가입 서비스를 구현했다.


      
   - 마이페이지 서비스
     
     <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
      
      
      Cash : 전체 부분을 총괄하는 클래스
          - 신청 정보 저장(saveFile), 신청 정보 불러오기(callFile), 가격 책정(paySelection)의 기능을 가진다.
      
      Collecter : 관리자, 쓰레기 수거 정보 입력
          - 관리자의 역할(유저 열람(searchUserFile) 등), 실제 도착 시간(setTimeSec)을 지정하는 기능을 가진다.

     위와 같은 클래스와 flask 및 파이썬을 활용하여 마이페이지 서비스르 만들다.
     마이페이지는 이용자가 어떤 쓰레기를 신청했는지, 가격은 얼마 나왔는지 등을 보여주는 페이지이다. 

     




### 시연 영상

https://youtu.be/t9rYfN6Y2ko

- 00:00 메인 페이지 소개

- 00:02 로그인 창 

- 00:03 회원가입 정보 기입

- 00:32 카드 결재 정보 기입

- 01:17 수거 정보 기입

- 02:44 마이 페이지를 통해 수거 현황 



