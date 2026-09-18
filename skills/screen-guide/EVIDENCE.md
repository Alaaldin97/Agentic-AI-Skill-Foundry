# Evidence for screen-guide

## Positive test

### Prompt

```text
/screen-guide

I want to cancel an app subscription from this screen.
Using only this screenshot as the starting point, tell me the full step-by-step path of where to tap until I reach the cancellation option.
Also tell me what I should expect to see after each tap.
Do not ask me for another screenshot unless you truly cannot continue safely.
```

### Transcript

```text
From this Settings screen:

1. Scroll all the way to the top of the page.
   You should see your Apple ID profile row with your name and profile picture.

2. Tap your name / Apple ID profile row at the top.
   A page with your Apple account details will open.

3. Tap "Subscriptions".
   You should see a list of your active and expired App Store subscriptions.

4. Tap the app subscription you want to cancel.
   The subscription management page will open.

5. Tap "Cancel Subscription".
   iOS should display a confirmation prompt.

6. Confirm the cancellation.
   The page should then indicate that the subscription is canceled.
```

### Why this proves activation

The user provided a screenshot of a software interface and asked for a complete click-by-click navigation path.

This is exactly what screen-guide is designed to handle.

**Did it activate on its own?** No — this run was explicitly invoked with
`/screen-guide`, so it demonstrates that the skill *behaves* correctly once
loaded, not that the router selects it unprompted. Automatic trigger behaviour
still needs to be tested with a natural-language prompt that does not name the
skill, for example: *"I'm on this screen and I want to cancel my subscription —
where do I tap?"* with the screenshot attached and nothing else.

## Dormancy test

### Near-miss prompt

```text
What is in this image?
```

### Transcript

```text
The image shows a cream-colored Golden Retriever puppy sitting and facing the camera against a black background.
```

### Why this proves dormancy

The user only asked for a description of a normal image.

The request was not about navigating a software interface, so screen-guide stayed quiet and did not fire.