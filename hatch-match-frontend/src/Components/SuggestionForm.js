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
    const [catchImage, setCatchImage] = useState(null)
    const [social, setSocial] = useState('')

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
            setCatchImage(null)
            setShowThanks(!showThanks)
        } catch (error) {
            console.error('Error submitting suggestion:', error);
        }
    };

    const handleCatchSubmit = async (e) => {
        e.preventDefault();

        const catchFormData = new FormData();
        catchFormData.append('catch_image', catchImage);
        catchFormData.append('social', social);

        try {
            await axios.post('http://localhost:5000/api/catch_of_week', catchFormData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setImage(null)
            setShowThanks(!showThanks)
        } catch (error) {
            console.error('Error submitting:', error);
        }
    }

    function handleNameChange(e) {
        setName(e.target.value)
    }

    function handleImageChange(e) {
        setImage(e.target.files[0]);
    };

    function handleImitationChange(e) {
        setSelectedImitation(e.target.value)
    }

    function handleLifeCycleChange(e) {
        setSelectedLifeCycle(e.target.value)
    }

    function handleCatchImageChange(e) {
        setCatchImage(e.target.files[0]);
    }

    function handleSocialChange(e) {
        setSocial(e.target.value)
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
        <div className='Uploads'>
            <div className='form-container'>
                <h2>Suggestion Box</h2>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="name">Fly Name:</label><br />
                    <input type="text" id="name" name="name" value={name} onChange={handleNameChange} /><br /><br />
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
                <ThanksPopUp showThanks={showThanks} setShowThanks={setShowThanks} image={image} catchImage={catchImage}/>
            </div>
            <div>
                <h2>Catch of the Week Upload</h2>
                <form onSubmit={handleCatchSubmit}>
                    <label htmlFor='catch_image'>Catch Image:</label><br />
                    <input type='file' id='catch_image' name='catch_image' onChange={handleCatchImageChange} /><bgr />
                    <label htmlFor='social'>Social Media Link:</label><br />
                    <input type='text' id='social' name='social' value={social} onChange={handleSocialChange} /><br />
                    <button type='submit'>Submit</button>
                </form>
            </div>
        </div>
    );
};

export default SuggestionForm;