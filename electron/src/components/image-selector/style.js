import styled from 'styled-components';

export const ImageWrapper = styled.aside`
  display: block;
  width:90%;
  margin:50px auto 0px auto;
  color:#61dafb;
  text-transform:uppercase;
  text-align:center;
  font-size:14px;
  border-radius:8px;

  .dropzone{
    width:100%;
    padding:20px;
    border: 1px dashed #61dafb;
  }
`;

export const ThumbsContainer = styled.div`
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    margin-top: 16;
 `;
  
  export const Thumb = styled.div`
    display: inline-flex;        
    width: 100%;
    max-width:500px;
    max-width:100%;
    height: 100%;
    margin-top:8px;    
    text-align:center;
  `;
  
  export const ThumbInner = styled.div`
    display: flex;
    min-width: 100%;
    overflow: hidden;    
  `;
  

  export const ImgStyle = styled.img`
    display: block;
    height: 100%;
    width:100%;
    max-height:400px;
    object-fit:fill;
    margin:0px auto;
    text-align:center;
    border: 1px solid #61dafb;
    transition:all 0.2s ease-in-out;
    `;