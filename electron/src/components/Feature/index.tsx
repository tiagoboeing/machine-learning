import React, { useEffect, useState } from "react";
import * as S from "./styles";

interface Props {
  data?: any;
  loadingData: boolean;
}

interface Characteristics {
  name: string;
  value: number;
}

const Feature: React.FC<Props> = ({ data, loadingData }) => {
  const [characteristics, setCharacteristics] = useState([]);
  const [predictionResult, setPredictionResult] = useState({
    accuracy: 0,
    label: "",
  });

  useEffect(() => {
    console.log("data", data);
    if (data) {
      const parsedCharacteristics: any = Object.keys(data.features).map(
        (el: any) => ({
          name: el,
          value: data.features[el],
        })
      );
      if (parsedCharacteristics.length)
        setCharacteristics(parsedCharacteristics);

      setPredictionResult(data.prediction);
    }
  }, [data]);

  return (
    <S.Container>
      {!loadingData ?
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

          <S.Wrapper style={{ marginTop: "15px" }}>
            <div>
              <S.Subtitle>Predição</S.Subtitle>
              <S.List>
                <S.ListItem>{predictionResult.accuracy}</S.ListItem>
              </S.List>
            </div>
            <div>
              <S.Subtitle>Personagem</S.Subtitle>
              <S.List>
                <S.ListItem>{predictionResult.label}</S.ListItem>
              </S.List>
            </div>
          </S.Wrapper>
        </S.Content>
        :
        <p>Carregando...</p>
      }
    </S.Container>
  );
};

export default Feature;
