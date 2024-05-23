import React, { useState, useEffect } from 'react';

function DataFetcher() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => {
            setData(data);
            setLoading(false);
        });
    }, []); // Empty array ensures this effect runs once on mount

    if (loading) {
        return <p>loading...</p>
    }

    return (
        <ul>
            {date.map(item => (
                <li key={item.id}>{item.name}</li>
            ))}
        </ul>
    );
}

export default DataFetcher;
