import React from 'react'
import icon from '../assets/icon.png'

const Navbar = () => {
  return (
    <div className='flex justify-start items-center h-20 bg-(--md-sys-color-surface) text-(--md-sys-color-on-surface) gap-5 px-5'>
      <img src={icon} className='w-20 h-20 rounded-full'/>
      <span style={{ fontFamily: 'Lobster, cursive' }} className='text-2xl'>Lyric Match</span>
    </div>
  )
}

export default Navbar