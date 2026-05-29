FROM python:3.11-slim as builder

WORKDIR /tmp
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


#fial stage
FROM python:3.11-slim

# Create non-root user (security best practice)
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY app/ .

# Set permission
RUN chown -R appuser:appuser /app
# Use non-root user
USER appuser

# Add local pip installations to PATH
ENV PATH=/home/appuser/.local/bin:$PATH

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["python", "app.py"]