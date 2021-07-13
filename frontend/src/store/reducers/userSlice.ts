import { createSlice } from '@reduxjs/toolkit'
import User from '../../interfaces/userInterface';

const initialState: User = undefined;

export const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
  },
})

// Action creators are generated for each case reducer function
export const { } = userSlice.actions

export default userSlice.reducer