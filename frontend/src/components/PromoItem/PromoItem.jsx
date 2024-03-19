import style from './PromoItem.module.scss';

const PromoItem = ({ image, label }) => {
  return (
    <div className={style.item}>
      <img src={image} alt={image} className={style.image} />
      <p className={style.label}>{label}</p>
    </div>
  );
};

export default PromoItem;
