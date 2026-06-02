import sys
from dotenv import load_dotenv
from generator import generate_postmortem

load_dotenv()

def main():
    if len(sys.argv) > 1:
        incident = " ".join(sys.argv[1:])
    else:
        print("Describe the incident (blank line to finish):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        incident = "\n".join(lines)

    if not incident.strip():
        print("No incident provided.")
        sys.exit(1)

    print("\nGenerating post-mortem...\n")
    result = generate_postmortem(incident)
    print(result)

    with open("postmortem.md", "w") as f:
        f.write(result)
    print("\nSaved to postmortem.md")

if __name__ == "__main__":
    main()
