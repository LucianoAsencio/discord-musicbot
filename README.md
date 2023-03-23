# discord-music-gpt-bot
Un proyecto de un bot de discord capaz de reproducir canciones de youtube y contestarte utilizando la API de OpenAI con ChatGPT

<img src="https://i.imgur.com/SGnLMHp.jpg">

## **¿Cómo funciona?**

Una vez que el bot está ingresado en nuestro servidor de discord, escribimos el comando:<br>

    .play "url"
    
Donde "url" es un link de youtube.<br><br>
**Por ejemplo:** 

    .play https://www.youtube.com/watch?v=dQw4w9WgXcQ

## **¿Cómo hacer mi propio bot?**

Para hacer tu propio bot de discord tenés que:
- Ingresar a la [web de desarrollador de discord](https://discord.com/developers/applications)
- Crear una nueva aplicación y ponerle un nombre.
- Ir a la sección de bots y clickear "Add bot".
- Sin cambiar de página clickea "Copy Token" y guardalo en un lugar seguro.
- Instala las siguientes librerías:

        discord.py
        ffmpeg
        PyNaCl
        yt-dlp
        openai
        
 - Cloná el repositorio
 
        git clone www.github.com/LucianoAsencio/discord-musicbot.git
        
 - Declará tu token como variable de entorno
 
        set BOT_TOKEN="tu_token"
        
- Conseguí una clave de API de OpenAI.
- Declará tu clave como variable de entorno

         set OPENAI_API_KEY="tu_api_key"
        
 - Descargá FFMpeg y pasale la ruta en el parametro "executable", en main.py.

        ... executable="C:/Tu/Ruta/ffmpeg.exe"...
        
 Ingresá tu bot a tu server de discord desde la web de desarrollador de discord, ejecutá main.py y listo!
 
Ya tenés un bot de discord completamente funcional que puede reproducir canciones de youtube, te contesta tus dudas y preguntas mediante una integración con la API de OpenAI con el modelo gpt-turbo-3.5 y obvio, es completamente configurable!
 
 Cualquier duda, consulta o pregunta me la pueden hacer por acá, [Linkedin](www.linkedin.com/in/luciano-asencio) o por [mail](lucianoasencio01@gmail.com)!
 


  
