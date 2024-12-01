import React from "react";
import styled, { ThemeProvider } from "styled-components";
import GlobalStyle from "./global";
import { theme } from "./theme";
// Styled Components
const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #000b58;
  color: #e6e9af;
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

const Button = styled.button`
  width: 200px;
  padding: 1rem 0;
  font-size: 1.5rem;
  font-weight: bold;
  color: #000b58;
  background-color: #e6e9af;
  border-radius: 10px;
  border: 2px solid #e6e9af;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background-color: #fffacd;
    color: #000b58;
  }
`;

const App = () => {
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

export default App;