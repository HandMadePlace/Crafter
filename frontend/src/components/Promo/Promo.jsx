import teamwork from '../../assets/img/Teamwork of company employees.png';
import discus from '../../assets/img/Team of employees discussing the project.png';
import selfie from '../../assets/img/Young woman taking a selfie.png';
import highFive from '../../assets/img/people giving each other a high five.png';
import PromoItem from '../PromoItem/PromoItem';
import logo from '../../assets/img/Logo.png';
import craftVibe from '../../assets/img/CraftVibe.png';
import style from './Promo.module.scss';
import Button from '../Button/Button';

const items = [
  { id: 1, image: teamwork, label: 'Знайдете унікальні товари' },
  { id: 2, image: selfie, label: 'Познайомите світ з вами' },
  { id: 3, image: discus, label: 'Отримаєте гідну оплату' },
  { id: 4, image: highFive, label: 'Покажіть ваші неймовірні вироби' },
];

const Promo = () => {
  return (
    <div className={style.container}>
      <div className={style.white}>
        <img src={logo} alt="logo" width="102px" />
        <img
          src={craftVibe}
          alt="logoName"
          width="230px"
          className={style.logoName}
        />
        <p className={style.promoText}>на нашій платформі ви:</p>
      </div>
      <div className={style.gradient}>
        {items.map((item) => (
          <PromoItem image={item.image} label={item.label} key={item.id} />
        ))}
      </div>
      <div className={style.button}>
        <Button
          name="Додати оголошення"
          variant="contained"
          textColor="black"
          textSize="large"
          color="orange"
        ></Button>
      </div>
    </div>
  );
};

export default Promo;
