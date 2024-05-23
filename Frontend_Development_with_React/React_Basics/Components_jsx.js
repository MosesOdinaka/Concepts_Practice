// Functional Component using JSX
import React from 'react';

function Greeting(props) {
    return <h1>Hello, {props.name}!</h1>;
}

export default Greeting;

// Usage in another component
import React from 'react';
import Greeting from './Greeting';

function App() {
    return (
        <div>
            <Greeting name="Alice" />
            <Greeting name="Bob" />
        </div>
    );
}

export default App;
