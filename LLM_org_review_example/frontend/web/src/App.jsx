
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import {useState, useEffect} from 'react';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';
import fetch_google_reviews from './services/fetch_google_reviews';

import './App.css'

function App() {

  const [organization_name, setOrganization_name] = useState("ntt_docomo") 
  const [result, setResult] = useState({"data" : {organization: '', reviews: [], 'llm_response' : ''}})
  


  const handleSubmit = async (event) => {
    console.log("Button clicked")
    console.log(organization_name)

     try{
          const get_data = await fetch_google_reviews(organization_name)
          console.log(get_data.data)
          setResult(get_data.data)
        } 
        catch (error){
          console.log("ERROR MESSAGE : " + error)
        }
        finally{
          console.log("REQUEST ENDED")
        }
  }

  return (
    <>

    
    {/*  #ffde23	(255,222,35)
          #fff071	(255,240,113)
          #f6ffd2	(246,255,210)
          #d7f47b	(215,244,123)
          #8ccb3b	(140,203,59)
        
          */}
        
    <Box
      sx={{
        width: "100%",
        maxWidth:800,
        margin: "2% auto",
        padding: 5,
        backgroundColor: '#fff071',
        borderRadius: '10px'
      }}
    >
      <Box
        sx={{
          width:"90%",
          margin: "3% auto",
          padding: 1,

          borderRadius: '10px',
          backgroundColor: '#917a3ce5',
          fontSize:20,
          color:'#ffffff',
        }}
        >
          By pairing LangChain framework with Ollama's local LLM execution, this tool automates the complete evaluation of organization reviews. It accepts raw feedback as input and parses it for core themes, sentiment, and workplace performance metrics. The workflow outputs an overall calculated rating paired with an in-depth qualitative analysis of the organization.
      </Box>
      <Divider sx={{}}/>
      <TextField
        fullWidth
        label="Organization Name"
        placeholder="Enter Organization Name"
        sx={{backgroundColor:'#f6ffd2'}}
        value={organization_name}
        onChange={(event) => setOrganization_name(event.target.value)}
      />

      <Button
        variant="contained"
        fullWidth
        onClick={handleSubmit}
        sx={{ marginTop: 2, backgroundColor:'#8ccb3b'}}
      >
        Submit
      </Button>

          <Divider />
        <Box
        sx={{
          width:"90%",
          textAlign: "center",
          margin : '2% auto',
          padding : '2%',
          backgroundColor:'#d7f47b',
          borderRadius : '10px'
        }}
        >

         
          <div>Result from <strong>Ollama LLM </strong>(Model : <strong>llama3.1:latest</strong>)</div>
          <div>{result.data && result.data.reviews.length > 0 ? (
            <div>Rating: {result.llm_response.rating}<br/>{result.llm_response.analysis_by_llm}</div>
          ) : (<div>No response from LLM yet</div>)}</div>

          <Divider sx={{margin : '3%'}} />
          <div><strong>Prompt Stats </strong></div>
          {result.status == 200 ? (
            <div><div>Prompt length: {result.prompt_stats.prompt_length}<br/></div>
          <div>Prompt length: {result.prompt_stats.prompt_token_count}</div>
          <div>Total execution time: {result.prompt_stats.execution_time.toFixed(3)} sec</div></div>
        ) : (
                <div>No stats available</div>
          )}
          <Divider sx={{margin : '3%'}} />
          {result && result.data.reviews.length > 0 ? (
          
          <div>
            <div>Here are the reviews from <b>{result.data.organization}</b></div>
            <Divider sx={{margin : '2%'}} />
            {result.data.reviews.map((item) => (
            <div><strong>{item.id} : {item.comment}<br/></strong></div>
          ))}</div>
         ) : (
          <div>No reviews available</div>
         )}

          <Divider sx={{margin : '3%'}} />

        </Box>
    </Box>
    </>
  )
}

export default App
