import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import { generateLyrics, checkGuess } from '../services/operations/songAPI';
import bg from '../assets/bg.jpg';
// eslint-disable-next-line no-unused-vars
import { AnimatePresence, motion } from "framer-motion";


const Home = () => {
	const [showLyrics, setShowLyrics] = useState(false);
	const [lyrics, setLyrics] = useState('');
	const [songId, setSongId] = useState(null);
	const [guess, setGuess] = useState('');
	const [result, setResult] = useState(null);
	const [guessMade, setGuessMade] = useState(false);
	const [loading, setLoading] = useState(false);

	const handleGenerateLyrics = async () => {
		setLoading(true);
		const response = await generateLyrics();
		setLoading(false);

		if (response && response.lyric_snippet) {
			setLyrics(response.lyric_snippet);
			setSongId(response.song_id);
			setShowLyrics(true);
			setGuess('');
			setResult(null);
			setGuessMade(false);
		}
	};

	const handleCheckGuess = async () => {
		const response = await checkGuess({ song_name: guess, song_id: songId });
	
		if (response) {
			if (response.message === "Correct guess! 🎉") {
				setResult("Correct!");
			} else {
				setResult(`Incorrect! The correct song is: ${response.correct_song}`);
			}
			setGuessMade(true);
		}
	};
  
	return (
		<>
		<Navbar />
		<div style={{ fontFamily: 'Poppins, sans-serif' }} className='flex flex-col items-center justify-center h-[calc(100vh-5rem)] gap-10 bg-neutral-900'>

			<h1 style={{ fontFamily: 'Lobster, sans-serif' }} className='text-6xl font-bold text-neutral-50'>Lyric Match</h1>
			<AnimatePresence>
			{!loading && !showLyrics && (
				<motion.div
				className="flex flex-col items-center text-center space-y-4"
				initial={{ opacity: 1, height: "auto" }}
				animate={{ opacity: 1, height: "auto" }}
				exit={{ opacity: 0, height: 0 }}
				transition={{ duration: 0.5, ease: "easeInOut" }}
				>
					<motion.h1
					className="text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-500"
					style={{ fontFamily: "Montserrat, cursive" }}
					>
						Decode the Lyrics, Unleash the Melody
					</motion.h1>

					<motion.p
					className="text-lg text-neutral-300 max-w-4xl"
					style={{ fontFamily: "Poppins, sans-serif" }}
					>
						Where every snippet holds a secret, and every guess brings you closer to the music. <span className="material-icons text-white align-middle">music_note</span>
					</motion.p>
				</motion.div>
			)}
			</AnimatePresence>

			<motion.div 
			initial={{ height: '4px' }}
			animate={{ height: loading || showLyrics ? '60vh' : '4px' }}
			transition={{ duration: 1, ease: 'easeInOut' }}
			className='flex text-center justify-center items-center w-[65%] h-[60vh] rounded-3xl overflow-hidden bg-cover bg-center bg-no-repeat relative' 
			style={{ 
				backgroundImage: showLyrics ? `url(${bg})` : 'none',
				backgroundColor: showLyrics ? 'transparent' : 'white' 
			}}
			>

				{(showLyrics || loading) && 
				<div className="absolute inset-0 bg-black/75 backdrop-blur-lg  flex items-center justify-center p-6">
					{loading ? (
					<div className="flex flex-col items-center">
						<motion.div
						initial={{ scale: 0.5, opacity: 0.1 }}
						animate={{ scale: 1, opacity: 1 }}
						transition={{ duration: 1, repeat: Infinity, repeatType: "reverse" }}
						className="text-5xl"
						>
						🎵
						</motion.div>
						<p className="mt-3 text-xl text-white">Generating lyrics...</p>
					</div>
					) : (
					<pre className='text-2xl text-amber-50 font-semibold text-center'>{lyrics}</pre>
					)}
				</div>
				}
				
			</motion.div>

			
			<div className='flex justify-center items-center gap-10'>
				{!showLyrics || guessMade ? (
				<button 
				className='w-60 h-15 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-bold py-4 px-6 rounded-4xl shadow-lg cursor-pointer hover:from-purple-600 hover:to-blue-600 transition-all'
				onClick={handleGenerateLyrics} 
				disabled={loading}
				>
					Generate Lyric Snippet
				</button>

				) : (
				<>
				<input 
				type="text" 
				placeholder="Guess the song"
				value={guess}
				onChange={(e) => setGuess(e.target.value)}
				className="w-150 h-15 p-3 text-white bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all"
				/>

				<button 
				className="w-45 h-15 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-bold py-4 px-6 rounded-4xl shadow-lg cursor-pointer hover:from-purple-600 hover:to-blue-600 transition-all"
				onClick={handleCheckGuess}
				>
				Check Answer
				</button>
				</>
			)}
			</div>
			{result && <p className='text-xl font-bold text-amber-50'>{result}</p>}
		</div>
		</>
	);
};

export default Home;
