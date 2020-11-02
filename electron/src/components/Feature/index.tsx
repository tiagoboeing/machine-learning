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
  const [response, setResponse] = useState({
    features: [],
    audioname: "",
    result: ""
  });

  useEffect(() => {
    if (data) {
      console.log("RESULT", Object.keys(data.features))
      setResponse(data);
    }
  }, [data]);

  return (
    <S.Container>
      {!loadingData && response ? (
        <S.Content>
          <header>Características</header>
          {response.features && (
            <S.Wrapper style={{ marginBottom: "50px" }}>
              <div>
                <S.List>
                  {Object.keys(response.features).map((item: any, index) => (
                    <S.ListItem key={index}>
                      {item} = {(response.features as any)[item]}
                    </S.ListItem>
                  ))}
                </S.List>
              </div>
            </S.Wrapper>
          )}
          {response && <p>Resultado da classificação: <strong>{response.result == 'cat' ? "GATO" : "CÃO"}</strong></p>}

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
