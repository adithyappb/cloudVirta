import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ContainerManagement() {
    const [containers, setContainers] = useState([]);

    useEffect(() => {
        axios.get('/api/containers')
            .then(response => setContainers(response.data))
            .catch(error => console.error('Error fetching containers:', error));
    }, []);

    return (
        <div>
            <h1>Containers</h1>
            <ul>
                {containers.map(container => (
                    <li key={container.id}>{container.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default ContainerManagement;

