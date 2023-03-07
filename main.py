import openai
import discord
from discord.ext import commands






token = ''

bot = commands.Bot(command_prefix="?!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    try:
        print("Online")
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)
        

        
    
    
    

@bot.hybrid_command(name="generate" , description="Text to Image Generator")
async def translate(ctx, *, prompt):
    
    # Load your API key from an environment variable or secret management service
    
    try:
        print(prompt)
        prompt = prompt.split()
        prompt_text = " ".join(prompt)
        openai.api_key = ""
        response = openai.Image.create(prompt=prompt_text, n=3, size="1024x1024")
        image_url = response['data'][0]['url']
        await ctx.reply(image_url)
    except openai.error.InvalidRequestError:
        await ctx.reply("u either typed in something racist, sexist, NSFW or all of the above 💀")
    
    
@bot.hybrid_command(name="ask" , description="ChatGPT assistant")
async def ask(ctx, *, prompt):
    print("performed ask task")
    
    # Load your API key from an environment variable or secret management service
    
    openai.api_key = ""
    conv= [{"role": "system", "content": "You are a helpful assistant."}]
    
    conv.append({"role": "user", "content": prompt})
    
    responds = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= conv,
    temperature=0.3,
    )
    
    conv.append({"role": "assistant", "content": responds['choices'][0]['message']['content']})
    response_text = responds['choices'][0]['message']['content']
    while response_text:
        await ctx.reply(response_text[:2000])
        response_text = response_text[2000:]
    print(responds['choices'][0]['message']['content'])

bot.run(token)
