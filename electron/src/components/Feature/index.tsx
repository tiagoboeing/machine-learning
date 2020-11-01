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
      console.log("RESULT", Object.keys(data.features))
      setResult(data);
    }
  }, [data]);

  return (
    <S.Container>
      {!loadingData && result ? (
        <S.Content>
          <header>Características</header>
          {result.features && (
            <S.Wrapper style={{ marginBottom: "50px" }}>
              <div>
                <S.List>
                  {Object.keys(result.features).map((item, index) => (
                    <S.ListItem key={index}>
                      {item} = {result.features[item]}
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
            {loadingData ? <p>Aguarde, classificando áudio...</p> : <p>...</p>}
          </div>
        )}
    </S.Container>
  );
};

export default Feature;
