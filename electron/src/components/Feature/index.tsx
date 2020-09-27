import React, { useEffect, useState } from "react";
import * as S from "./styles";

interface Props {
  data?: any;
}

interface Characteristics {
  name: string;
  value: number;
}

const Feature: React.FC<Props> = ({ data }) => {
  const [characteristics, setCharacteristics] = useState([]);

  useEffect(() => {
    console.log("data", data);
    if (data) {
      const parsed: any = Object.keys(data).map((el: any) => ({
        name: el,
        value: data[el],
      }));
      if (parsed.length) setCharacteristics(parsed);
    }
  }, [data]);

  return (
    <S.Container>
      <S.Content>
        <header>Características</header>
        <S.Wrapper>
          <div>
            <S.Subtitle>Bart</S.Subtitle>
            <S.List>
              {characteristics.length > 0 &&
                characteristics
                  .slice(0, 3)
                  .map((item: Characteristics, index) => (
                    <S.ListItem key={index}>
                      {item.name} = {item.value.toPrecision(4)}
                    </S.ListItem>
                  ))}
            </S.List>
          </div>
          <div>
            <S.Subtitle>Homer</S.Subtitle>
            <S.List>
              {characteristics.length > 0 &&
                characteristics
                  .slice(3, 6)
                  .map((item: Characteristics, index) => (
                    <S.ListItem key={index}>
                      {item.name} = {item.value.toPrecision(4)}
                    </S.ListItem>
                  ))}
            </S.List>
          </div>
        </S.Wrapper>
      </S.Content>
    </S.Container>
  );
};

export default Feature;
