import styled from "styled-components";

export const Container = styled.div`
  height: 100%;
  width: 100%;
  color: #fff;

  p {
    color: #2ecc71;
    font-size: 18px;
  }
`;

export const Content = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.5rem 1.5rem;

  header {
    font-size: 1.2rem;
    font-weight: 600;
    text-align: left;
    padding-bottom: 1.8rem;
  }
`;

export const Wrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
`;

export const Title = styled.h2`
  text-transform: uppercase;
  margin-bottom: 0.825rem;
`;

export const Subtitle = styled.h4`
  text-transform: uppercase;
  margin-bottom: 0.825rem;
`;

export const List = styled.div`
  display: flex;
  flex-direction: column;
`;

export const ListItem = styled.div`
  padding: 0.1rem;
`;
