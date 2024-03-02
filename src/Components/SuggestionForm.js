import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ThanksPopUp from './ThanksPopUp';
import '../Styles/suggestionForm.css'


const SuggestionForm = () => {
    const [name, setName] = useState('');
    const [image, setImage] = useState(null);
    const [showThanks, setShowThanks] = useState(false)
    const [selectedImitation, setSelectedImitation] = useState('')
    const [selectedLifeCycle, setSelectedLifeCycle] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('name', name);
        formData.append('imitation', selectedImitation);
        formData.append('life_cycle', selectedLifeCycle);
        formData.append('image', image);

        try {
            await axios.post('http://localhost:5000/api/submit', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setShowThanks(!showThanks)
        } catch (error) {
            console.error('Error submitting suggestion:', error);
        }
    };

    function handleImageChange(e) {
        setImage(e.target.files[0]);
    };

    function handleImitationChange(e) {
        setSelectedImitation(e.target.value)
    }

    function handleLifeCycleChange(e) {
        setSelectedLifeCycle(e.target.value)
    }

    useEffect(() => {
        function handleEscapeKey(event) {
            if (event.key === 'Escape') {
                setShowThanks(false);
            }
        }
        window.addEventListener('keydown', handleEscapeKey);
        return () => {
            window.removeEventListener('keydown', handleEscapeKey);
        };
    }, []);

    return (
        <div>
            <div className='form-container'>
                <h2>Suggestion Box</h2>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="name">Fly Name:</label><br />
                    <input type="text" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)} /><br /><br />
                    <label htmlFor='imitation'>Imitation:</label>
                    <select value={selectedImitation} onChange={handleImitationChange}>
                        <option> </option>
                        <option value='Mayfly'>Mayfly</option>
                        <option value='Caddis'>Caddis</option>
                        <option value='Stonefly'>Stonefly</option>
                        <option value='Midge'>Midge</option>
                        <option value='Terrestrials'>Terrestrials</option>
                        <option value='Baitfish'>Baitfish</option>
                    </select>
                    <label htmlFor='life cycle'>Life Cycle:</label>
                    <select value={selectedLifeCycle} onChange={handleLifeCycleChange}>
                        <option> </option>
                        <option value='Nymph'>Nymph</option>
                        <option value='Emerger'>Emerger</option>
                        <option value='Adult'>Adult</option>
                    </select>
                    
                    <label htmlFor="image">Upload Image:</label><br />
                    <input type="file" id="image" name="image" onChange={handleImageChange} /><br /><br />
                    <button type="submit">Submit</button>
                </form>
            </div>
            <div>
                <ThanksPopUp showThanks={showThanks} setShowThanks={setShowThanks}/>
            </div>
        </div>
    );
};

export default SuggestionForm;