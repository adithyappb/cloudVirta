import React, { useEffect, useState } from 'react';
import axios from 'axios';

function VMManagement() {
    const [vms, setVMs] = useState([]);

    useEffect(() => {
        axios.get('/api/vms')
            .then(response => setVMs(response.data))
            .catch(error => console.error('Error fetching VMs:', error));
    }, []);

    return (
        <div>
            <h1>Virtual Machines</h1>
            <ul>
                {vms.map(vm => (
                    <li key={vm.id}>{vm.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default VMManagement;

