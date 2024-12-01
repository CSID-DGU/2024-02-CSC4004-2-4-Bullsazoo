import React from 'react';
import styled from "styled-components";
import GlobalStyle from './../styles/global';
import Kenwoo from './../assets/images/kenwoo.svg';
import Jeayong from './../assets/images/jeayong.svg';
import Kyeongsub from './../assets/images/kyeongsub.svg';
import Keonmin from './../assets/images/keonmin.svg';
import Minseong from './../assets/images/minseong.svg';
import Eye_icon from './../assets/images/Eye_icon.svg';

/*            주석부분은 global 컴포넌트로 대체 할거 같아서 주석 처리 해놨음
const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 1976px;;
  width: 430px;
  background-color: #000b58;
`;

const Card = styled.div`
  width: 400px;
  height: 200px;
  background-color: #000b58;
  border-radius: 20px;
  left: calc(50% - 400px/2);
  text-align: center;
`;
*/

const Header = styled.div`
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 20px;
  text-align: center;
  color: #FFFFFF;
`;

const Icon = styled.div`
  position: absolute;
  width: 120px;
  height: 120px;
  left: calc(50% - 120px/2);
  top: 134px;
  background: #000B58;
  border-radius: 4px;
`;

const ImageBox = styled.div`
  width: 400px;
  height: 200px;
  background-color: #ffffff;
  border-radius: 10px;
  margin: 10px 0;
`;

const Footer = styled.div`
  margin-top: 20px;
`;

const TeamSection = styled.div`
  width: 380px;
  height: 674px;
  left: 25px;
  top: 1210px;

  h3 {
    margin-bottom: 10px;
    font-family: 'NanumSquareRoundOTF';
    font-style: normal;
    font-weight: 800;
    font-size: 20px;
    line-height: 23px;
    text-align: center;
    color: #FFE31A;
  }

  .member {
    display: flex;
    align-items: center;
    margin-bottom: 10px;

    img {
      width: 100px;
      height: 100px;
      border-radius: 20%;
      margin-right: 10px;
    }

    div {
      font-family: 'NanumSquareRoundOTF';
      font-style: normal;
      font-weight: 800;
      font-size: 16px;
      line-height: 18px;
      color: #FFFFFF;
    }
  }
`;

const Landing_About = () => {
  return (
    <>
      <GlobalStyle />
      <Header>시각 장애인을 위한<br />쇼핑, 일상 보조 서비스 </Header>
      <Icon><img src={Eye_icon} alt="eye_icon" /></Icon>
      <ImageBox></ImageBox>
      <ImageBox />
      <ImageBox />
      <ImageBox />
      <Footer>OSSP Team NeverDie_4</Footer>
      <TeamSection>
        <h3>BE | Back-End Team member</h3>
        <div className="member">
          <img src={Jeayong} alt="jeayong" />
          <div>
            신재용<br />LD / BE / AI<br />YOLO 모델 학습
          </div>
        </div>
        <div className="member">
          <img src={Kyeongsub} alt="Kyeongsub" />
          <div>
            김경섭<br />BE / AI<br />모델 설계 / 홍보 / 배포
          </div>
        </div>
        <div className="member">
          <img src={Keonmin} alt="keonmin" />
            <div>
              이건민<br />BE / AI<br />TTS / STT 모델 설계 / 학습
            </div>
          </div>
        <h3>FE | Front-End Team member</h3>
        <div className="member">
          <img src={Kenwoo} alt="kenwoo" />
          <div>
            강근우<br />PM / Design / FE<br />개발 문서 작성/레이아웃 구성 / 통신
          </div>
        </div>
        <div className="member">
          <img src={Minseong} alt="minseong" />
            <div>
              김민성<br />PM / FE<br />레이아웃 구성 / 배포
            </div>
          </div>
      </TeamSection>
    </>
  );
};

export default Landing_About;