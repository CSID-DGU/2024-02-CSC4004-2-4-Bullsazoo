import React from "react";
import styled, { ThemeProvider } from "styled-components";
import GlobalStyle from "./../styles/global";
import { theme } from "./../styles/theme";


const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #000b58;
  color:#FFE31A;
`;

const LogoSection = styled.div`
  text-align: center;
  margin-bottom: 2rem;
`;

const Logo = styled.div`
  font-size: 4rem;
  margin-bottom: 0.5rem;
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
`;

const ButtonContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const Button = GlobalStyle.Button;

const LandingP = () => {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Container>
        <LogoSection>
          <Logo><img src={Eye_icon} alt="eye_icon" /></Logo>
          <Subtitle>당신의 시각 도우미</Subtitle>
        </LogoSection>
        <ButtonContainer>
          <Button>설명</Button>
          <Button>가입</Button>
          <Button>시작</Button>
        </ButtonContainer>
      </Container>
    </ThemeProvider>
  );
};

export default LandingP;