import React, { useEffect } from 'react';

import * as S from './styles';

interface Props {
  data?: [];
}

const Feature: React.FC<Props> = ({ data }) => {
  useEffect(() => {
    console.log('data ');
  }, [data]);

  return (
    <S.Container>
      <S.Content>
        <header>Caracteristicas</header>
        <S.Wrapper>
          <div>
            <S.Subtitle>Bart</S.Subtitle>
            <S.List>
              {data &&
                data.length > 0 &&
                data.map((item, index) => (
                  <S.ListItem key={index}>{item}</S.ListItem>
                ))}
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
