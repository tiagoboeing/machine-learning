import React, {useEffect, useState} from 'react';
import {useDropzone} from 'react-dropzone';
import {ImageWrapper, ThumbsContainer, Thumb, ThumbInner, ImgStyle} from './style';

export default function ImageSelector(props) {
  const [files, setFiles] = useState([]);
  const {getRootProps, getInputProps} = useDropzone({
    accept: 'image/*',
    onDrop: acceptedFiles => {
      acceptedFiles[0] && props.changeImage(acceptedFiles[0]);
      setFiles(acceptedFiles.map(file => Object.assign(file, {
        preview: URL.createObjectURL(file)
      })));
    }
  });
  
  const thumbs = files.map(file => (
    <Thumb key={file.name}>
      <ThumbInner>
          <ImgStyle
          src={file.preview}          
        />
      </ThumbInner>
    </Thumb>
  ));

  useEffect(() => () => {
    // Make sure to revoke the data uris to avoid memory leaks
    files.forEach(file =>URL.revokeObjectURL(file.preview));    
  }, [files]);

  return (
    <ImageWrapper>
      <div {...getRootProps({className: 'dropzone'})}>
        <input {...getInputProps()} />
        <p>Arraste ou Selecione sua Imagem</p>       
      </div>
      <ThumbsContainer>
        {thumbs}
      </ThumbsContainer>
    </ImageWrapper>
  );
}