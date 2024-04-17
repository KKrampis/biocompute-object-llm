from bcorag import pipeline
from bcorag import misc_functions as misc_fns

def main():

    logger = misc_fns.setup_root_logger("./logs/bcorag.log")
    logger.info('################################## RUN START ##################################')
    
    # get the user choices
    user_picks = pipeline.initalize_step()
    if user_picks is None:
        misc_fns.graceful_exit()

    # handle domain generation
    bco_rag = pipeline.retrieve_bco_rag(user_picks) # type: ignore
    response = bco_rag.choose_domain(automatic_query=True)
    if response is None:
        misc_fns.graceful_exit()

if __name__ == "__main__":
    main()
