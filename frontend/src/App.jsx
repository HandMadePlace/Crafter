import './App.css';
import Button from './components/Button/Button';

function App() {
  return (
    <div>
      <Button name="Клієнтам" variant="text" textColor="black"></Button>
      <Button
        name="Додати оголошення"
        variant="contained"
        textColor="black"
        textSize="large"
        color="orange"
        disabled
      ></Button>
    </div>
  );
}

export default App;
