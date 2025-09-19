#https://subnp.com/free-api

// Make the request
const response = await fetch("/api/free/generate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    prompt: "A beautiful sunset over mountains",
    model: "turbo"
  })
});

// Create event source for streaming updates
const reader = response.body
  .pipeThrough(new TextDecoderStream())
  .pipeThrough(new TransformStream({
    transform(chunk, controller) {
      // Parse SSE data
      const lines = chunk.split('\n');
      const messages = lines
        .filter(line => line.startsWith('data: '))
        .map(line => JSON.parse(line.slice(6)));
      
      messages.forEach(data => {
        switch (data.status) {
          case 'processing':
            console.log('Progress:', data.message);
            break;
          case 'complete':
            console.log('Image URL:', data.imageUrl);
            break;
          case 'error':
            console.error('Error:', data.message);
            break;
        }
      });
    }
  }));

// Start reading the stream
reader.read();