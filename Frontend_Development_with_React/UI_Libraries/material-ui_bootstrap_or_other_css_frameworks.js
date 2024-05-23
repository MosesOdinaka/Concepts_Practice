// Installing Material-UI
// npm install @material-ui/core

import React from 'react';
import { Button } from '@material-ui/core';

function App() {
    return (
        <div>
            <Button variant="contained" color="primary">Material-UI Button</Button>
        </div>
    );
}

export default App;

// Install Bootstrap
// npm install bootstrap
// In your index.js or App.js, import Bootstrap CSS
import 'bootstrap/dist/css/bootstrap.min.css';

import React from 'react';

function App() {
    return (
        <div className='container'>
            <button className='btn btn-primary'>Bootstrap Button</button>
        </div>
    );
}

export default App;
