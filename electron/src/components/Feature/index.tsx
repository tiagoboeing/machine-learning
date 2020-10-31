import React, { useEffect, useState } from "react";
import * as S from "./styles";

interface Props {
  data?: any;
  loadingData: boolean;
  type: string;
}

interface Features {
  name: string;
  value: number;
}

const Feature: React.FC<Props> = ({ data, loadingData }) => {
  const [result, setResult] = useState(null);

  useEffect(() => {
    if (data) {
      setResult(data);
    }
  }, [data]);

  return (
    <S.Container>
      {!loadingData && result ? (
        <S.Content>
          <header>Classificação</header>
          {result.features.length > 0 && (
            <S.Wrapper style={{ marginBottom: "50px" }}>
              <div>
                <S.Subtitle>Cão</S.Subtitle>
                <S.List>
                  {result.features.map((item: Features, index) => (
                    <S.ListItem key={index}>
                      {item.name} = {item.value.toPrecision(4)}
                    </S.ListItem>
                  ))}
                </S.List>
              </div>
            </S.Wrapper>
          )}
          {result && <p>Resultado da classificação: <strong>{result.result == 'cat' ? "GATO" : "CÃO"}</strong></p>}

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
            <p>Aguarde, classificando áudio...</p>
          </div>
        )}
    </S.Container>
  );
};

export default Feature;
