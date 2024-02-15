import classNames from 'classnames';
import './Button.scss';

const Button = (props) => {
  const {
    name,
    variant,
    disabled,
    onClick,
    color,
    textSize,
    textColor,
    startIcon,
    endIcon,
  } = props;

  const buttonClasses = classNames('button', {
    text: variant === 'text',
    contained: variant === 'contained',
    outlined: variant === 'outlined',
    orange: color === 'orange',
    grey: color === 'grey',
    blue: color === 'blue',
    lightBlue: color === 'lightBlue',
    small: textSize === 'small',
    large: textSize === 'large',
    white: textColor === 'white',
    black: textColor === 'black',
    
  });
  return (
    <button className={buttonClasses} onClick={onClick} disabled={disabled}>
      {startIcon && startIcon}
      {name}
      {endIcon && endIcon}
    </button>
  );
};

export default Button;
