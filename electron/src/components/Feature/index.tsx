import React from 'react';

import * as S from './styles';

const Feature: React.FC = () => {
  return (
    <S.Container>
      <S.Content>
        <header>Caracteristicas</header>
        <S.Wrapper>
          <div>
            <S.Subtitle>Bart</S.Subtitle>
            <S.List>
              <S.ListItem>Cu</S.ListItem>
              <S.ListItem>Zao</S.ListItem>
              <S.ListItem>Né?</S.ListItem>
            </S.List>
          </div>
          <div>
            <S.Subtitle>Homer</S.Subtitle>
            <S.List>
              <S.ListItem>De</S.ListItem>
              <S.ListItem>Li</S.ListItem>
              <S.ListItem>Cia</S.ListItem>
            </S.List>
          </div>
        </S.Wrapper>
      </S.Content>
    </S.Container>
  );
};

export default Feature;
