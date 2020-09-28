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
      {!loadingData ? (
        <S.Content>
          <header>Características</header>

          {characteristics.length > 0 && (
            <S.Wrapper style={{ marginBottom: "50px" }}>
              <div>
                <S.Subtitle>Apu</S.Subtitle>
                <S.List>
                  {characteristics
                    .slice(0, 3)
                    .map((item: Characteristics, index) => (
                      <S.ListItem key={index}>
                        {item.name} = {item.value.toPrecision(4)}
                      </S.ListItem>
                    ))}
                </S.List>
              </div>

              <div>
                <S.Subtitle>Marge</S.Subtitle>
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
          )}

          {!!predictionResult.label && (
            <S.Wrapper style={{ marginTop: "15px" }}>
              <div style={{ width: "320px" }}>
                <S.Subtitle>Personagem</S.Subtitle>
                <S.List>
                  {predictionResult.label.toLowerCase() === "apu" ? (
                    <img src="assets/img/apu.jpg" width="100%" />
                  ) : predictionResult.label.toLowerCase() === "marge" ? (
                    <img src="assets/img/marge.jpg" width="100%" />
                  ) : (
                    "Não identificado"
                  )}
                </S.List>
              </div>

              <div
                style={{
                  marginLeft: "20px",
                  alignItems: "center",
                  display: "flex",
                }}
              >
                <S.List>
                  <S.ListItem style={{ marginBottom: "10px" }}>
                    A predição retornou uma acurácia de{" "}
                    <b>{predictionResult.accuracy.toPrecision(2)}%</b>
                  </S.ListItem>
                  <S.ListItem>
                    <div>Personagem identificado</div>
                    <div>
                      <b>{predictionResult.label}</b>
                    </div>
                  </S.ListItem>
                </S.List>
              </div>
            </S.Wrapper>
          )}
        </S.Content>
      ) : (
        <div
          style={{
            width: "100%",
            height: "100%",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <p>Aguarde, classificando imagem...</p>
        </div>
      )}
    </S.Container>
  );
};

export default Feature;
